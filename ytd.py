#/usr/bin/env python

#importing functions
from turtle import clear
import ytd_functions as ytdf
from datetime import datetime
import time as t
from pytube import YouTube
from pytube.cli import on_progress
import argparse
import sys


def check_arguments():

    
    
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='')

    group = parser.add_mutually_exclusive_group()

    parser.add_argument('--url','-u', type=str, help='Valid Youtube video URL', required=True)

    group.add_argument('--audio','-a', help='Audio stream', action='store_true', default='void')
    group.add_argument('--video','-v', help='Video stream', action='store_true', default='void')
    parser.add_argument('--start','-s', type=str, help='Start point for trimming', default='void')
    parser.add_argument('--end','-e', type=str, help='End point for trimming', default='void')
    parser.add_argument('--output','-o', type=str, help='Output file name', default='standard')

    args = parser.parse_args()

    yt = YouTube(args.url,on_progress_callback=on_progress)

    if args.video == "void":
        if args.start == "void":
            ytdf.download_audio(yt,args.output)
        else:
            ytdf.cut_audio(yt,args.start, args.end, args.output)
    else:
        if args.start == "void":
            ytdf.download_video(yt,args.output)
        else:
            ytdf.cut_video(yt, args.start, args.end, args.output)

    

def check_args():
    if not len(sys.argv) > 1:
        main()
    else: 
        check_arguments()

#main thread
def main():

    file_name = ""

    #main menu
    while True:
        
        while True:
            ytdf.header(ytdf.standard_header, True)
            url = input(" - Insert Youtube video URL: ")
            if ytdf.check_url(url): break
            else: print(ytdf.CRED + "> Invalid parameter!" + ytdf.CEND) ; t.sleep(1)
            ytdf.clear_screen()

        yt = YouTube(url, on_progress_callback=on_progress)

        ytdf.header(ytdf.standard_header, True)
        ytdf.header(ytdf.CBLUE + f"> Target - {yt.title}" + ytdf.CEND)
        print("(1) - Download Full Video")
        print("(2) - Download and Trim Video")
        print("(3) - Download Full Audio")
        print("(4) - Download and Trim Audio")
        print("(q) - Quit")
        user_option = input("Option: ")

        match user_option:
            case "1":

                while True:
                    
                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header(ytdf.CBLUE + f"> Target - {yt.title}" + ytdf.CEND)
                    ytdf.header("> Download Full Video")
                    
                    file_name = input("- File output name: ")
                    if file_name == "" : file_name = f"{yt.title}"
                    break
                
                ytdf.download_video(yt,file_name)
                ytdf.wrapping(f"{file_name}.mp4")

            case "2":

                while True:

                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header(ytdf.CBLUE + f"> Target - {yt.title}" + ytdf.CEND)
                    ytdf.header("> Download and Trim video")
                    
                    file_name = input("- File output name: ")
                    if file_name == "" : file_name = f"{yt.title}"

                    start = input("- Start point (HH:MM:SS): ")
                    end = input("- End point (HH:MM:SS): ")

                    if ytdf.check_timestamps(url, start, end):
                        ytdf.cut_video(yt,start, end, file_name)
                        ytdf.wrapping(f"{file_name}.mp4")
                        break

            case "3":

                while True:
                    
                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header(ytdf.CBLUE + f"> Target - {yt.title}" + ytdf.CEND)
                    ytdf.header("> Download Full Audio")
                    
                    file_name = input("- File output name: ")
                    if file_name == "" : file_name = f"{yt.title}"
                    break
                
                ytdf.download_audio(yt,file_name)
                ytdf.wrapping(f"{file_name}.mp4")

            case "4":

                while True:

                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header(ytdf.CBLUE + f"> Target - {yt.title}" + ytdf.CEND)
                    ytdf.header("> Download and Trim audio")
                    
                    file_name = input("- File output name: ")
                    if file_name == "" : file_name = f"{yt.title}"

                    start = input("- Start point (HH:MM:SS): ")
                    end = input("- End point (HH:MM:SS): ")

                    if ytdf.check_timestamps(url, start, end):
                        ytdf.cut_audio(yt,start, end, file_name)
                        ytdf.wrapping(f"{file_name}.mp4")
                        break
        
            case ("q"|"quit"):
                print("Exiting now...")
                t.sleep(1)

            case _: 
                print("Insert a valid option...") ; t.sleep(1)

        if user_option.lower() == "q" or user_option.lower() == "quit":
            break

if __name__ == "__main__":
   check_args()
