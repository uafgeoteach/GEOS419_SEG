## Helper functions for reading and parsing JHU-APL EZIE Mag data.

# Importing required libraries.
import glob
import pandas as pd
import zipfile
import os
import shutil

def unzip_ezie_files(name, filepath, merge):
    '''
    name (string): The name of the EZIE-Mag kit, i.e., geos1, geos2, geos3.
    filepath (string): Location of the daily/weekly files.
    merge (bool): If True, the unzipped files will be merged under one folder.

    returns:  folderpath
    '''
    ezie_zip_files = glob.glob(filepath+'*.zip')
    output_folderlist = []

    for file in ezie_zip_files:
        
        output_filename = filepath+name+'_'+file.split('/')[-1].split('.')[1]
        print('Writing zip file as ', output_filename, '.')

        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(output_filename)
        
        print('File unzipped in filepath.')
        output_folderlist.append(output_filename)

    if merge:
        print('Merging files under one folder.')
        
        merged_filepath = filepath+name+'_merged'
        if not os.path.exists(merged_filepath):
            os.makedirs(merged_filepath)

        for folder in output_folderlist:
            search_paths = glob.glob(os.path.join(folder, '*', '*', 'smr.60s', '*'))
            print('Searching for hourly files in ', search_paths)
            for path in search_paths:
                ezie_hourly_files = glob.glob(os.path.join(path, '*smr.60s.txt'))
                for hourly_file in ezie_hourly_files:
                    shutil.copy(hourly_file, merged_filepath)

        return(merged_filepath)

    else:
        print('Merging declined by user. To merge unzipped files under folder, select merge=True.')


def read_and_parse_ezie_mag_data(filename):

    """
    Reads and parses JHU-APL EZIE Mag data.

    Arguments:
        filename (string): The full path to filename.

    EZIE Data Column Names:
        ezie_cols ='timeString, tval, intt, nsamp, stid, fingerprint, latitude, longitude, altitude, tres, ctemp, ccr, Bx, By, Bz, afs_sel, fs_sel, Ax, Ay, Az, Gx, Gy, Gz, imu_ctemp'

    Returns:
        Parsed hourly file as a pandas dataframe. 

    """

    ezie_cols ='timeString, tval, intt, nsamp, stid, fingerprint, latitude, longitude, altitude, tres, ctemp, ccr, Bx, By, Bz, afs_sel, fs_sel, Ax, Ay, Az, Gx, Gy, Gz, imu_ctemp'.split(', ')

    ezie_hourly_file = pd.read_csv(filename, names=ezie_cols, header=None, sep=" ")
    ezie_hourly_file['timeString'] = pd.to_datetime(ezie_hourly_file['timeString'])
    return ezie_hourly_file

def merge_eziemag_data(filepath):
    '''
    Merges the files in the folder and returns a single dataframe.
    
    Arguments: 
        filepath (string): The location of the hourly files.

    Returns:
        Merged dataframe of all hourly files in the folder.

    '''

    filelist = glob.glob(filepath+'/'+'*smr.60s.txt')
    filelist.sort()
    print('There are ', len(filelist),' files in the folder.')
    ezie_hourly_list = []

    for file in filelist:
        ezie_hourly_list.append(read_and_parse_ezie_mag_data(file))
    
    #ezie_hourly_data = [df.set_index('id') for df in ezie_hourly_list]
    ezie_merged_df = pd.concat(ezie_hourly_list, axis=0)
    ezie_merged_df.reset_index(inplace=True)
    return ezie_merged_df
