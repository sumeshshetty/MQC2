import boto3
s3_res=boto3.resource('s3',region_name='ap-south-1')
def download_s3_object(url):
	try:
		# a="https://zee5transcoding-source-staging2.s3.ap-south-1.amazonaws.com/mp4/elemental/TV_SHOWS/PREMIUM/Remodeling_Premium_testing_hi_88272c065008d25187ddce69a84fefdd_mp4/mp4.mp4"
		BucketName=url.split('/')[2].split('.')[0]
		print(f"BucketName: {BucketName}")
		S3Key=url.split('/',3)[3]
		print(f"S3Key: {S3Key}")
		ec2_local_path='/tmp/'+url.rsplit('/')[-1]
		print(f"ec2_local_path: {ec2_local_path}")
		response=s3_res.download_file(BucketName, S3Key,ec2_local_path)
		print(f"Download Complete: {response}")
	except Exception as err:
		print(f"Error in download_s3_object : {err}")
		

	return ec2_local_path