import csv
from sys import argv
from typing import List, Dict


def doubles(companies: List[str], prices: List[int], budget: int) -> List[List[str]]:
    """
    This function should
        1. Return a list containing all pairs of companies that sum up to budget
        2. Make use of a python dict / set(hash table)
        3. Have worst case time complexity O(N)[Assuming hash table insertion is constant]
    """

    complement_hash: Dict[int, List[str]] = {}
    pair_matches: List[List[str]] = []

    for i in range(len(companies)):
        company: str
        price: int

        company, price = companies[i], prices[i]
        diff_price: int = budget - price

        # Assumes stock price > 0
        # Ensures stock price < budget
        if diff_price > 0:
            if diff_price in complement_hash:
                for pair_company in complement_hash[diff_price]:
                    pair_matches.append([company, pair_company])
            else:
                complement_hash.setdefault(price, list()).append(company)

    return pair_matches


def triples(companies: List[str], prices: List[int], budget: int) -> List[List[str]]:
    """
    This function should
        1. Return a list containing all triplets of stock names with prices that sum up to budget
        2. Have worst case time complexity O(N^2) [Assuming hash table insertion is constant]

    Hint: If your doubles function runs in O(N) time, think about how you can call it in triples
    """

    lookup_hash: Dict[int, List[List[str]]] = {}
    triple_matches: List[List[str]] = []

    for i in range(len(companies)):
        company: str
        price: str

        company, price = companies[i], prices[i]
        diff_price: int = budget - price

        # Assumes stock price > 0
        # Ensures stock price < budget
        if diff_price > 0:
            any_matches: List[List[str]] = lookup_hash.setdefault(
                diff_price,
                doubles(
                    companies[i + 1:],
                    prices[i + 1:],
                    diff_price
                )
            )

            if any_matches:
                for pair_matches in any_matches:
                    triple_matches.append([company, *pair_matches])

    return triple_matches


def main():
    if len(argv) != 3:
        print('missing filename or budget as command line argument')
        return

    filename = argv[1]
    budget = int(argv[2])

    companies = []
    prices = []
    with open('prices/' + filename, 'r') as csv_file:
        myReader = csv.reader(csv_file)
        lineCount = 0
        for row in myReader:
            if lineCount == 0:
                lineCount += 1
                continue

            companies.append(row[0])
            prices.append(int(row[1]))

    print("doubles result:", doubles(companies, prices, budget))
    print()
    print("triples result:", triples(companies, prices, budget))


if __name__ == "__main__":
    main()
