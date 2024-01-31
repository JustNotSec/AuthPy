import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor
import os
import tkinter as tk
import ctypes

def validate_license():
    license_url = "https://cf32cdb2-0c6e-4bdc-8ca2-37908f3ea252-00-qm62wjzxtt8d.spock.replit.dev/license.txt"
    namaLicense = input("Masukan License Nya: ")
    try:
        response = requests.get(license_url)
        if response.status_code == 200:
            license_content = response.text
            # Check if the license content is valid (you can modify this based on your license format)
            if f"{namaLicense}" in license_content:
                return license_content
    except Exception as e:
        print("License validation failed:", str(e))
    return None

def main():
  license_content = validate_license()
    if license_content:
        print("Connected with license:", license_content)
    else:
        print("License validation failed. Exiting...")
        return
