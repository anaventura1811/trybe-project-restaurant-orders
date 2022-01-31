from .utils.restaurant_utils import (
    get_most_ordered_dish_by_client,
    how_often_dish_was_ordered,
    never_been_at_restaurant,
    list_never_ordered_dishes
    )


def analyze_log(path_to_file):
    try:
        marias_most_ordered_dish = get_most_ordered_dish_by_client(
            'maria', path_to_file
        )
        arnaldo_hmb_count = how_often_dish_was_ordered(
            'arnaldo',
            'hamburguer',
            path_to_file
        )
        joaos_never_ordered_dishes = list_never_ordered_dishes(
            'joao',
            path_to_file
        )
        joao_not_at_restaurant = never_been_at_restaurant(
            'joao', path_to_file)
        with open(file="data/mkt_campaign.txt", mode='w') as log_file:
            log_file.writelines(
                f"{marias_most_ordered_dish}\n" +
                f"{arnaldo_hmb_count}\n" +
                f"{joaos_never_ordered_dishes}\n" +
                f"{joao_not_at_restaurant}\n"
            )
    except NotImplementedError:
        raise NotImplementedError


# analyze_log('data/orders_1.csv')
