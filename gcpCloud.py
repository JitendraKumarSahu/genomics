from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import json
from cloud import Cloud 

from google.cloud import dataproc_v1
from google.cloud.dataproc_v1.gapic.transports import (
    cluster_controller_grpc_transport)
from google.cloud.dataproc_v1.gapic.transports import (
    job_controller_grpc_transport)


class GcpCloud(Cloud):
	""" GCP Cloud Infrastructure class """
	waiting_callback = False

	def __init__(self, project_id, zone, cluster_name, global_region):
		self.project_id = project_id
		self.zone = zone
		self.cluster_name = cluster_name
		self.global_region = global_region
    	# [START dataproc_get_client]
		if global_region:
			print("Global...")
			self.region = 'global'
			# Use the default gRPC global endpoints.
			self.dataproc_cluster_client = dataproc_v1.ClusterControllerClient()
			self.dataproc_job_client = dataproc_v1.JobControllerClient()
		else:
			print("Regional...")
			self.region = self.get_region_from_zone()
			# Use a regional gRPC endpoint. See:
			# https://cloud.google.com/dataproc/docs/concepts/regional-endpoints
			self.client_transport = (
				cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
					address='{}-dataproc.googleapis.com:443'.format(self.region)))
			self.dataproc_cluster_client = dataproc_v1.ClusterControllerClient(
				self.client_transport)
			self.dataproc_cluster_client.from_service_account_file('BioDock-52fc17a3ee5d.json')
		# [END dataproc_get_client]

	def get_region_from_zone(self):
		try:
			region_as_list = self.zone.split('-')[:-1]
			return '-'.join(region_as_list)
		except (AttributeError, IndexError, ValueError):
			raise ValueError('Invalid zone provided, please check your input.')

	def callback(self, operation_future):
		# Reset global when callback returns.
		self.waiting_callback = False

	def wait_for_cluster_creation(self):
		"""Wait for cluster creation."""
		print('Waiting for cluster creation...')
		print(self.waiting_callback)
		while True:
			if not self.waiting_callback:
				print("Cluster created.")
				break

	# [START dataproc_create_cluster]
	def create_cluster(self):
		"""Create the cluster."""
		print('Creating cluster...')
		self.zone_uri = \
			'https://www.googleapis.com/compute/v1/projects/{}/zones/{}'.format(
				self.project_id, self.zone)
		with open('config.json', 'r') as f:
			self.cluster_data = json.load(f)

		self.cluster_data['project_id'] = self.project_id
		self.cluster_data['cluster_name'] = self.cluster_name
		self.cluster_data['config']['gce_cluster_config']['zone_uri'] = self.zone_uri

		self.cluster = self.dataproc_cluster_client.create_cluster(self.project_id, self.region, 
						self.cluster_data)
		self.cluster.add_done_callback(self.callback)
		self.waiting_callback = True
		self.wait_for_cluster_creation()
	# [END dataproc_create_cluster]

	# [START dataproc_list_clusters_with_detail]
	def list_clusters_with_details(self):
		"""List the details of clusters in the region."""
		print("List the details of clusters in the region.")
		for cluster in self.dataproc_cluster_client.list_clusters(self.project_id, self.region):
			print(('{} - {}'.format(cluster.cluster_name,
								cluster.status.State.Name(
									cluster.status.state))))
	# [END dataproc_list_clusters_with_detail]

	# [START dataproc_delete]
	def delete_cluster(self):
		"""Delete the cluster."""
		print('Tearing down cluster.')
		result = self.dataproc_cluster_client.delete_cluster(
				project_id=self.project_id, region=self.region, cluster_name=self.cluster_name)
		return result
	# [END dataproc_delete]

	def get_cluster_id_by_name(self):
		"""Helper function to retrieve the ID and output bucket of a cluster by
			name."""
		for cluster in self.dataproc_cluster_client.list_clusters(projectId, region):
			if cluster.cluster_name == cluster_name:
				return cluster.cluster_uuid, cluster.config.config_bucket


