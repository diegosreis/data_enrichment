import argparse
import os

import pandas as pd

from services.enricher_service import EnricherService


def save_result(dataset, output_path):
    dataset.to_csv(output_path, index=False)
    print(f"Result saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Enrich data from a CSV datasets',
        epilog='Example usage: python script.py path/to/your/file.csv --output file'
    )
    parser.add_argument('file_path', help='Path to the CSV file')
    parser.add_argument('--output', choices=['screen', 'file'], default='screen',
                        help='Whether to display on the screen or save the result to a file')

    args = parser.parse_args()

    try:
        dataset = pd.read_csv(args.file_path)
    except FileNotFoundError:
        print(f"Error: The file {args.file_path} was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file {args.file_path} is empty.")
        return

    enrich_service = EnricherService()
    enriched_dataset = enrich_service.enrich_data(dataset)

    if not enriched_dataset.empty:
        if args.output == 'file':
            output_dir = 'output'
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "enriched_result.csv")
            save_result(enriched_dataset, output_path)
        else:
            print(enriched_dataset)
    else:
        print("Error: Failed to enrich the dataset.")


if __name__ == "__main__":
    main()
