import sys
from pathlib import Path
import pandas as pd



import rtree
import gdal


gdal_version_num = int(gdal.VersionInfo('VERSION_NUM'))
print(f'gdal version number is {gdal_version_num}.')


from azureml.pipeline.wrapper.dsl.module import ModuleExecutor, InputDirectory, OutputDirectory
from azureml.studio.core.io.data_frame_directory import load_data_frame_from_directory
from azureml.pipeline.wrapper import dsl

@dsl.module(
    name="gdal_sample"
)
def gdal_sample(
        output_dir1: OutputDirectory(),
        output_dir2: OutputDirectory(),
        input_dir1: InputDirectory(),
        input_dir2: InputDirectory()
):
    print('module definition')
    print(f'input_dir1: {Path(input_dir1).resolve()}')
    print(f'input_dir2: {Path(input_dir2).resolve()}')
   

    
    dfd1 = load_data_frame_from_directory(input_dir1)
    data_frame1 = dfd1.data
    print(data_frame1.head(10))


if __name__ == '__main__':
    ModuleExecutor(gdal_sample).execute(sys.argv)
