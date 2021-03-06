from top_stores.aggregations import TopStoresAggregator


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
