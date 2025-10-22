import csv
import os
from pathlib import Path

from langfuse import Langfuse


def get_langfuse_client() -> Langfuse:
    """Initialize Langfuse client with environment variables."""
    return Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST"),
    )


def ensure_dataset_exists(dataset_name: str, langfuse_client: Langfuse, csv_file_path: str = None) -> None:
    """
    Ensure a dataset exists in Langfuse, creating it if necessary.
    
    Args:
        dataset_name: Name of the dataset
        langfuse_client: Initialized Langfuse client
        csv_file_path: Optional path to CSV file for metadata
    """
    try:
        # Try to get the dataset to check if it exists
        langfuse_client.get_dataset(dataset_name)
        print(f"Dataset '{dataset_name}' already exists")
    except Exception:
        # Dataset doesn't exist, create it
        print(f"Creating new dataset: {dataset_name}")
        
        metadata = {
            "type": "evaluation",
            "source": "tagesschau"
        }
        
        if csv_file_path:
            metadata["csv_file"] = Path(csv_file_path).name
        
        langfuse_client.create_dataset(
            name=dataset_name,
            description=f"Evaluation dataset: {dataset_name}",
            metadata=metadata
        )
        print(f"Dataset '{dataset_name}' created successfully")


def upload_csv_dataset(csv_file_path: str, dataset_name: str, langfuse_client: Langfuse) -> None:
    """
    Upload a CSV dataset to Langfuse.
    
    Args:
        csv_file_path: Path to the CSV file
        dataset_name: Name for the dataset in Langfuse
        langfuse_client: Initialized Langfuse client
    """
    print(f"Uploading dataset: {dataset_name} from {csv_file_path}")
    
    # Ensure the dataset exists before uploading items
    ensure_dataset_exists(dataset_name, langfuse_client, csv_file_path)
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row_idx, row in enumerate(csv_reader):
            try:
                # Extract data from CSV row
                input_text = row.get('input', '')
                expected_output = row.get('expected_output', '')
                expected_articles = row.get('expected_articles', '')
                
                # Create dataset item
                langfuse_client.create_dataset_item(
                    dataset_name=dataset_name,
                    input={
                        "text": input_text
                    },
                    expected_output={
                        "text": expected_output
                    },
                    metadata={
                        "expected_articles": expected_articles,
                        "row_index": row_idx
                    }
                )
                
                if (row_idx + 1) % 10 == 0:
                    print(f"  Uploaded {row_idx + 1} items...")
                    
            except Exception as e:
                print(f"Error uploading row {row_idx}: {e}")
                continue
    
    print(f"Finished uploading dataset: {dataset_name}")


def upload_all_tagesschau_datasets() -> None:
    """Upload all CSV datasets from the tagesschau directory to Langfuse."""
    
    # Initialize Langfuse client
    langfuse_client = get_langfuse_client()
    
    # Define the CSV directory path
    csv_dir = Path("src/advanced_rag/evaluation/datasets/")
    
    if not csv_dir.exists():
        print(f"Directory not found: {csv_dir}")
        return
    
    # Get all CSV files in the directory
    csv_files = list(csv_dir.glob("*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {csv_dir}")
        return
    
    print(f"Found {len(csv_files)} CSV files to upload:")
    for csv_file in csv_files:
        print(f"  - {csv_file.name}")
    
    # Upload each CSV file as a separate dataset
    for csv_file in csv_files:
        # Use the filename (without extension) as the dataset name
        dataset_name = csv_file.stem
        
        try:
            upload_csv_dataset(str(csv_file), dataset_name, langfuse_client)
        except Exception as e:
            print(f"Failed to upload {csv_file.name}: {e}")
            continue
    
    # Flush to ensure all data is sent
    langfuse_client.flush()
    print("All datasets uploaded successfully!")


if __name__ == "__main__":
    upload_all_tagesschau_datasets()