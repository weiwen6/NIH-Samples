
# The following is an example of a command for downloading files from GDC using a manifest file:

gdc-client download -m  /Users/JohnDoe/Downloads/gdc_manifest_6746fe840d924cf623b4634b5ec6c630bd4c06b5.txt

#Downloading Data Using GDC File UUIDs 
#The GDC Data Transfer Tool also supports downloading of one or more individual files using UUID(s) instead of a manifest file. To do this, enter the UUID(s) after the download command:

gdc-client download 22a29915-6712-4f7a-8dba-985ae9a1f005

#Multiple UUIDs can be specified, separated by a space:

gdc-client download e5976406-473a-4fbd-8c97-e95187cdc1bd fb3e261b-92ac-4027-b4d9-eb971a92a4c3

#Resuming a Failed Download 
The GDC Data Transfer Tool supports resumption of interrupted downloads. To resume an incomplete download, repeat the download of the manifest or UUID(s) in the same folder as the initial download. Failed downloads will appear in the destination folder with a .partial extension. This feature allows users the ability to identify quickly where the download stopped. For large downloads this feature can let the user identify where the download was interrupted and edit the manifest accordingly.

gdc-client download f80ec672-d00f-42d5-b5ae-c7e06bc39da1
Downloading Controlled-Access Data 

#A user authentication token is required for downloading Controlled-Access Data from GDC. Tokens can be obtained from the GDC Data Portal (see instructions in Obtaining an Authentication Token). Once downloaded, the token file can be passed to the GDC Data Transfer Tool using the -t or --token-file option:

gdc-client download -m gdc_manifest_e24fac38d3b19f67facb74d3efa746e08b0c82c2.txt -t gdc-user-token.2015-06-17T09-10-02-04-00.txt

#Directory structure of downloaded files 
#The directory in which the files are downloaded will include folders named by the file UUID. Inside these folders, along with the the data and zipped metadata or index files, will exist a logs folder. The logs folder contains state files that insure that downloads are accurate and allow for resumption of failed or prematurely stopped downloads. While a download is in progress a file will have a .partial extension. This will also remain if a download failed. Once a file is finished downloading the extension will be removed. If an identical manifest is retried another attempt will be made to download files containing a .partial extension.

C501.TCGA-BI-A0VR-10A-01D-A10S-08.5_gdc_realn.bam.partial  logs