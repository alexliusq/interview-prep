

class SalesRankers:
    def get_ranking_by_product(product_id) -> dict:
        pass

    def get_products_by_category(category_id, rank_start) -> list:
        ## pagination
        pass

class UpdateSalesRankerBatchJob:

    def __init__(self,
                 num_worker: int = 10,
                 start_time: 'datetime',
                 time_between_runs: 'timedelta',
                 ):
        pass

    def run(transaction_db_uri: 'URI',
            product_info_db_uri: 'URI',
            days_to_look_back: int = 180,
            number_of_items_to_rank: int = 100,
    ):
        pass

class Redis:
    # store in chunks of 100 or so
    key = f'{category_id}_{rank_start}_{rank_end}'

    # todo: what's keys for product?
    product_key = f'{product_id}'

from typing import Enum


