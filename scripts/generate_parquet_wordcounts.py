import os
import pandas as pd
import argparse


def count_words_in_text_column(df, text_column="text"):
    total_words = 0
    for value in df[text_column].dropna():
        total_words += len(str(value).split())

    return total_words


def main(directory, output_csv="word_counts.csv", text_column="text"):
    results = []

    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.lower().endswith(".parquet"):
                full_path = os.path.join(root, fname)

                try:
                    df = pd.read_parquet(full_path)
                    word_count = count_words_in_text_column(df, text_column)
                    results.append({
                        "file": full_path,
                        "word_count": word_count
                    })
                except Exception as e:
                    print(f"Error processing {full_path}: {e}")

    if results:
        pd.DataFrame(results).to_csv(output_csv, index=False)
        print(f"Saved word counts to {output_csv}")
    else:
        print("No parquet files found or processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count words in all parquet files in a directory")
    parser.add_argument("--directory", "-d", required=True, help="Directory containing parquet files")
    parser.add_argument("--output", "-o", default="word_counts.csv", help="Output CSV file")

    args = parser.parse_args()

    main(directory=args.directory, output_csv=args.output)
