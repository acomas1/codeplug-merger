# Filename: scanlist_merge.py

# MIT License
# 
# Copyright (c) 2024 Andrew Comas (N2ZT)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import pandas as pd
import sys

def rename_duplicates(df, column_name):
    """
    Renames duplicate entries in the specified column by appending a suffix to the duplicate values.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column where duplicates need to be renamed.

    Returns:
    pandas.DataFrame: The DataFrame with renamed duplicates in the specified column.
    """
    # Generate a series of counts for each unique value in the column
    counts = df.groupby(column_name).cumcount()

    # Rename duplicates by appending the count (starting from 1) to the original value
    df[column_name] = df[column_name].where(counts == 0, df[column_name] + (counts + 1).astype(str))

    return df

def merge_csv(file1, file2, output_file='merged_file.csv'):
    # Check if the output file is writable
    try:
        with open(output_file, 'w') as f:
            pass
    except IOError:
        print(f"Error: The output file '{output_file}' is not writable.")
        sys.exit(1)

    # Load the CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ensure that the "No." column exists in both files
    if 'No.' not in df1.columns or 'No.' not in df2.columns:
        print("Error: Both CSV files must contain a 'No.' column.")
        sys.exit(1)

    # Remove rows where the "No." column equals 4001 or 4002 in both DataFrames
    df1 = df1[~df1['No.'].isin([4001, 4002])]
    df2 = df2[~df2['No.'].isin([4001, 4002])]

    # print(df1)
    # print(df1['No.'].max())
    # print(df2['No.'].max())

    # Get the last number from the "No." column of the first CSV file
    last_no_in_df1 = df1['No.'].max()

    # Update the "No." column in the second CSV file
    df2['No.'] = df2['No.'] + last_no_in_df1

    # Merge the DataFrames
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Remove duplicate rows based on the 'Zone  Name' column, keeping the first occurrence
    # merged_df = merged_df.drop_duplicates(subset='Zone Name', keep='first')

    # Rename duplicates in the 'Scan List Name' column
    merged_df = rename_duplicates(merged_df, 'Scan List Name')

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"Merged CSV file saved to {output_file}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python merge_csv.py <file1.csv> <file2.csv> [output_file.csv]")
        sys.exit(1)

    # Assign command-line arguments to variables
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # make sure files exists
    try:
        with open(file1, 'r') as f:
            pass
    except IOError:
        print(f"Error: The input file '{sys.argv[1]}' is not readable.")
        sys.exit(1)

    try:
        with open(file2, 'r') as f:
            pass
    except IOError:
        print(f"Error: The input file '{sys.argv[2]}' is not readable.")
        sys.exit(1)

    # Optional output file name, default is 'merged_file.csv'
    output_file = sys.argv[3] if len(sys.argv) > 3 else 'scanlist_merged_file.csv'

    # Call the merge function
    merge_csv(file1, file2, output_file)
