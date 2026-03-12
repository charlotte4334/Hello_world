'''This script reads a list of people and the courses they take and then 
grets each person for the pSciComp course
'''
import argparse
from types import SimpleNamespace
import os
from pathlib import Path

from exohw.utils import (load_json_file, load_config, prepare_output_dir
                        )
from exohw.hello import create_greetings as write_hello
def main() -> None:
    

    parser = argparse.ArgumentParser(description="Running hello world script")
    parser.add_argument("--config_file", type=str,default= os.environ.get("CONFIG_PATH"), help="Path to the config file")
    parser.add_argument("--input_json", type=str, default=os.environ.get("INPUT_JSON"), help="Path to the input json file")
    parser.add_argument("--output_dir", type=str, default=os.environ.get("OUTPUT_DIR"), help="Path to the output directory")
    args = parser.parse_args()

    # Resolve paths 
    if not args.config_file:
        raise ValueError("Config file path is not provided. Please set the CONFIG_PATH environment variable or provide it as an argument.")
    if not args.input_json:
        raise ValueError("Input JSON path is not provided. Please set the INPUT_JSON environment variable or provide it as an argument.")
    if not args.output_dir:
        raise ValueError("Output directory path is not provided. Please set the OUTPUT_DIR environment variable or provide it as an argument.")

    # 2. Execute core logic using the utilities
    #    - load config and create config namespace
    config_data = load_json_file(Path(args.config_file))
    cfg = load_config(config_data=config_data)
    #    - load input data
    people = load_json_file(Path(args.input_json))
    #    - ready output location
    out_dir = prepare_output_dir(args.output_dir)
    final_path = write_hello(people=people,
                             output_dir=out_dir,
                             cfg=cfg)
    
if __name__ == "__main__":
      main()