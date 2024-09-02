# codeplug-merger
Merge CSV files from CPS to create new codeplugs

These programs are designed to merge Anytone D878UVII Plus codeplug csv file.  The following csv files are supported:
        - Channel.csv
        - Zone.csv
        - Scanlist.csv
         - TalkGroups
- You will need to make sure the file names are unique.
- Duplicate Channel and TalkGroups will be dropped and only the first one will be kept.  This maybe a problem if the same name has different attributes
- Duplicate Zone, and ScanList will rename the second occurrence.    You will need to decide manually to keep them or not.
        
##Setup
- Best practice is load up the .rtf files in your CPS software  and export to different directories.  
- Then rename the files you want to merge and move them to the directory where you have installed the .py files
          -Generic syntax:
                        - Xxx_merge.py file1.csv file2.csv optional_output_filename.csv

Installation instruction
        ○ Go to the directory you have the channel_merge.py and your csv files
        ○ Install Python
        ○ Pip install pandas

    
Channel
    • Execution
        ○ Make sure you don't have your new file name open in another program like Excel
        ○ Make sure the 1st row of the 1st csv file has your Radio ID properly set
        ○ The code should keep the blank rows from both files in order.
        ○ Execution Syntax:
            § python channel_merge.py channel.csv channel_li.csv [optional_output_file.csv]
Zone
    • Execution
        ○ Make sure you don't have your new file name open in another program like Excel
        ○ The code should keep the blank rows from both files in order.
        ○ Execution Syntax:
            § python zone_merge.py zone.csv zone_li.csv [optional_output_file.csv]

ScanList
• Execution
    ○ Make sure you don't have your new file name open in another program like Excel
    ○ The code should keep the blank rows from both files in order.
    ○ Execution Syntax:
        § python scanlist_merge.py scanlist.csv scanlist_li.csv [optional_output_file.csv]
