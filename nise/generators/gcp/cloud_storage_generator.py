"""Module for gcp cloud storage data generation."""
from random import choice

from nise.generators.gcp.gcp_generator import GCPGenerator


class CloudStorageGenerator(GCPGenerator):
    """Generator for GCP Cloud Storage data."""

    STORAGE = (
        ('com.google.cloud/services/cloud-storage/StorageRegionalUsGbsec', 'byte-seconds',
         'Regional Storage US'),
        ('com.google.cloud/services/cloud-storage/ClassARequestRegional', 'byte-seconds',
         'Class A Request Regional Storage'),
        ('com.google.cloud/services/cloud-storage/ClassBRequestRegional', 'byte-seconds',
         'Class B Request Regional Storage'),
        ('com.google.cloud/services/cloud-storage/BandwidthDownloadAmerica', 'bytes',
         'Download Worldwide Destinations (excluding Asia & Australia)')
    )

    def _update_data(self, row):  # pylint: disable=arguments-differ
        """Update a data row with storage values."""
        storage = choice(self.STORAGE)
        row['line_item'] = storage[0]
        row['measurement1'] = storage[0]
        row['measurement1_total_consumption'] = self.fake.pyint()  # pylint: disable=maybe-no-member
        row['measurement1_units'] = storage[1]
        row['cost'] = self.fake.pyint()  # pylint: disable=maybe-no-member
        row['currency'] = 'USD'
        row['description'] = storage[2]
        return row

    def generate_data(self):
        """Generate GCP storage data for some days."""
        days = self._create_days_list(self.start_date, self.end_date)
        data = {}
        for day in days:
            rows = []
            for _ in range(0, self.num_instances):
                row = self._init_data_row(day['start'], day['end'])
                row = self._update_data(row)
                rows.append(row)
            data[day['start']] = rows
        return data
