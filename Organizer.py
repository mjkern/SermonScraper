import os
import shutil
import pandas as pd

from Utilities import sanitize_filename

OUTPUT_DIR = "./McLean Pres Sermons"
BY_SPEAKER_DIR = f"{OUTPUT_DIR}/By Speaker"
BY_SERIES_DIR = f"{OUTPUT_DIR}/By Series"
EXCEL_PATH = f"{OUTPUT_DIR}/McLean Pres Sermons.xlsx"

def main():
    # get the csv of scraped data into a dataframe
    df = pd.read_csv('./output/outfile.csv')
    
    # sort sermons by speaker, creating symlinks by series
    paths = df.apply(axis = 1, func = lambda row: organize_audio_file(row['sermon_path'], row['series_dirname'], sanitize_filename(row['speaker']), row['sermon_filename']))

    # drop columns we don't want in the final output
    df = df.drop(columns=['series_dirname', 'series_path', 'sermon_filename', 'sermon_path', 'audio_link'])

    # include the new paths
    df['path_by_speaker'] = paths.apply(lambda d: d['path_by_speaker'])
    df['path_by_series'] = paths.apply(lambda d: d['path_by_series'])

    # reorder the columns
    df = df.reindex(columns=[
        'sermon_title',
        'speaker',
        'scripture',
        'series_title',
        'date',
        'sermon_link',
        'series_link',
        'path_by_speaker',
        'path_by_series'
    ])

    # write to excel doc for easy use
    df.to_excel(EXCEL_PATH, index=False)

def organize_audio_file(sermon_path, series_dirname, speaker_dirname, sermon_filename):
    """
    Organize the scaped audio into the desired file structure

    Notes
     - real files by speaker because IDK if symlinks will actually work
     - want sermons in their own subfolder so you can scroll through the names (instead of seek/skip)
     - symlinked sermons don't have their own subfolder beacuse seek/skip makes more sense here
    """
    
    # define the paths we want
    dest_dir = f"{BY_SPEAKER_DIR}/{speaker_dirname}/{sermon_filename}"
    link_dir = f"{BY_SERIES_DIR}/{series_dirname}"
    dest_path = f"{dest_dir}/{sermon_filename}.mp3"
    link_path = f"{link_dir}/{sermon_filename}.mp3"

    # ensure the paths exist
    os.makedirs(dest_dir)
    os.makedirs(link_dir, exist_ok=True)

    # copy and link the files
    shutil.copy(sermon_path, dest_path)
    os.symlink(dest_path, link_path)

    # return the paths
    return {'path_by_speaker': dest_path, 'path_by_series': link_path}

if __name__ == '__main__':
    main()