import operator
from collections import Counter, defaultdict
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
            A list of top stores records with fields `code_magasin` and `ca`.
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


class TopProductsAggregator:
    """
    Ingest transactions, aggregate most popular products per store, and query top n products by
    store.
    """

    def __init__(self):
        # Number of products by store
        self.stores_products = defaultdict(Counter)

        # Total revenue by product by store
        self.stores_products_revenue = defaultdict(lambda: defaultdict(float))

    def ingest(self, transaction: Dict[str, str]):
        """
        Ingest a transaction event.

        Args:
            transaction: the transaction, with mandatory keys `code_magasin`, `identifiant_produit`
                         and `prix`.
        """
        store_id = transaction['code_magasin']
        product_id = transaction['identifiant_produit']
        self.stores_products[store_id][product_id] += 1
        self.stores_products_revenue[store_id][product_id] += float(transaction['prix'])

    def get_top_products_by_store(self, n=10) -> Dict[str, List[Dict[str, str]]]:
        """
        Query top products by store.

        Args:
            n: number of top products to return by store.

        Returns:
            A dict that maps a store id to a list of top products records with fields
            `code_magasin`, `identifiant_produit` and `ca`.
        """

        top_products = {}

        for store_id, product_ids in self.stores_products.items():
            top_products[store_id] = top_products.get(store_id, [])
            for product_id, _ in product_ids.most_common(n):
                product_revenue = self.stores_products_revenue[store_id][product_id]
                top_products[store_id].append({
                    'code_magasin': store_id,
                    'identifiant_produit': product_id,
                    'ca': f'{product_revenue:.2f}'
                })

        return top_products
