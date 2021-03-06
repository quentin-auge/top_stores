import operator
from collections import defaultdict
from typing import Dict, List


class TopStoresAggregator:
    """
    Ingest transactions, aggregate total revenue by store, and query top n stores by revenue.
    """

    def __init__(self):
        # Total revenue by store
        self.stores_revenue = defaultdict(float)

    def ingest(self, transaction: Dict[str, str]):
        """
        Ingest a transaction event.

        Args:
            transaction: the transaction, with mandatory keys `code_magasin` and `prix`.
        """
        store_id = transaction['code_magasin']
        self.stores_revenue[store_id] += float(transaction['prix'])

    def get_top_stores(self, n=50) -> List[Dict[str, str]]:
        """
        Query top stores.

        Args:
            n: number of top stores to return.

        Returns:
            A list of top stores record with fields `code_magasin` and `ca`.
        """

        # Get top stores as a `(store_id, revenue)` list of tuples
        stores = self.stores_revenue.items()
        sorted_stores = sorted(stores, key=operator.itemgetter(1), reverse=True)
        top_stores = sorted_stores[:n]

        # Format output
        return [
            {
                'code_magasin': store_id,
                'ca': f'{revenue:.2f}'
            }
            for store_id, revenue in top_stores
        ]
