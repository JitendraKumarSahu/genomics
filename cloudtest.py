#!/usr/bin/env python3

import argparse
from gcpCloud import GcpCloud

def main(project_id,
         zone,
         cluster_name,
         create_new_cluster=True,
         global_region=True):

	cloudInfra = GcpCloud(project_id, zone, cluster_name, global_region)
	cloudInfra.create_cluster();
	cloudInfra.list_clusters_with_details()
	cloudInfra.delete_cluster()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.
                                     RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project_id', help='Project ID you want to access.', required=True)
    parser.add_argument('--zone',
                        help='Zone to create clusters in/connect to',
                        required=True)
    parser.add_argument('--cluster_name',
                        help='Name of the cluster to create/connect to',
                        required=True)
    parser.add_argument('--create_new_cluster',
                        action='store_true',
                        help='States if the cluster should be created')
    parser.add_argument('--global_region',
                        action='store_true',
                        help='If cluster is in the global region')
    '''
    parser.add_argument('--gcs_bucket',
                        help='Bucket to upload Pyspark file to',
                        required=True)
    parser.add_argument('--pyspark_file',
                        help='Pyspark filename. Defaults to pyspark_sort.py')
    '''

    args = parser.parse_args()
    main(args.project_id, args.zone, args.cluster_name, 
	 		args.create_new_cluster, args.global_region)
