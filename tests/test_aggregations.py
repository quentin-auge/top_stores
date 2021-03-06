from top_stores.aggregations import TopProductsAggregator, TopStoresAggregator


def test_top_stores_aggregator():
    aggregator = TopStoresAggregator()

    # Ingest and aggregate transactions

    aggregator.ingest({'code_magasin': 'A', 'prix': '1.1'})
    aggregator.ingest({'code_magasin': 'C', 'prix': '2.2'})
    aggregator.ingest({'code_magasin': 'A', 'prix': '3.3'})
    aggregator.ingest({'code_magasin': 'B', 'prix': '4.4'})
    aggregator.ingest({'code_magasin': 'D', 'prix': '5.5'})
    aggregator.ingest({'code_magasin': 'C', 'prix': '6.6'})
    aggregator.ingest({'code_magasin': 'A', 'prix': '7.7'})
    aggregator.ingest({'code_magasin': 'B', 'prix': '8.8'})
    aggregator.ingest({'code_magasin': 'D', 'prix': '9.9'})

    # Expected top stores

    expected_top_stores = [
        {'code_magasin': 'D', 'ca': '15.40'},
        {'code_magasin': 'B', 'ca': '13.20'},
        {'code_magasin': 'A', 'ca': '12.10'},
        {'code_magasin': 'C', 'ca': '8.80'}
    ]

    # Query top stores

    assert aggregator.get_top_stores(n=0) == []
    assert aggregator.get_top_stores(n=1) == expected_top_stores[:1]
    assert aggregator.get_top_stores(n=2) == expected_top_stores[:2]
    assert aggregator.get_top_stores(n=3) == expected_top_stores[:3]
    assert aggregator.get_top_stores(n=4) == expected_top_stores
    assert aggregator.get_top_stores(n=5) == expected_top_stores


def test_top_products_aggregator():
    aggregator = TopProductsAggregator()

    # Ingest and aggregate transactions

    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'a', 'prix': '1.1'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'c', 'prix': '2.2'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'b', 'prix': '3.3'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'c', 'prix': '4.4'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'a', 'prix': '5.5'})

    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'c', 'prix': '1.1'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'a', 'prix': '2.2'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'b', 'prix': '3.3'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'a', 'prix': '4.4'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'c', 'prix': '5.5'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'c', 'prix': '6.6'})

    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'b', 'prix': '6.6'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'b', 'prix': '7.7'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'a', 'prix': '8.8'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'c', 'prix': '9.9'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'a', 'prix': '10.10'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'b', 'prix': '11.11'})
    aggregator.ingest({'code_magasin': 'A', 'identifiant_produit': 'a', 'prix': '12.12'})

    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'b', 'prix': '7.7'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'c', 'prix': '8.8'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'a', 'prix': '9.9'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'b', 'prix': '10.10'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'c', 'prix': '11.11'})
    aggregator.ingest({'code_magasin': 'B', 'identifiant_produit': 'a', 'prix': '12.12'})

    # Expected top stores

    expected_top_products_store_A = [
        {'code_magasin': 'A', 'identifiant_produit': 'a', 'ca': '37.62'},
        {'code_magasin': 'A', 'identifiant_produit': 'b', 'ca': '28.71'},
        {'code_magasin': 'A', 'identifiant_produit': 'c', 'ca': '16.50'}
    ]

    expected_top_products_store_B = [
        {'code_magasin': 'B', 'identifiant_produit': 'c', 'ca': '33.11'},
        {'code_magasin': 'B', 'identifiant_produit': 'a', 'ca': '28.62'},
        {'code_magasin': 'B', 'identifiant_produit': 'b', 'ca': '21.10'}
    ]

    # Query top stores

    assert aggregator.get_top_products_by_store(n=0) == {'A': [], 'B': []}

    assert aggregator.get_top_products_by_store(n=1) == {
        'A': expected_top_products_store_A[:1],
        'B': expected_top_products_store_B[:1]
    }

    assert aggregator.get_top_products_by_store(n=2) == {
        'A': expected_top_products_store_A[:2],
        'B': expected_top_products_store_B[:2]
    }

    assert aggregator.get_top_products_by_store(n=3) == {
        'A': expected_top_products_store_A,
        'B': expected_top_products_store_B
    }

    assert aggregator.get_top_products_by_store(n=4) == {
        'A': expected_top_products_store_A,
        'B': expected_top_products_store_B
    }
