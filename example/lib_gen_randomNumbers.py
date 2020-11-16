import random

def generate_random_numbers():
    return random.randint(0,9)

def print_random_numbers():
    print(generate_random_numbers())

def join_random_pairs():
    join_pair_of_randoms = []
    for i in range(3):
        min_value = generate_random_numbers()
        max_value = generate_random_numbers()
        join_pair_of_randoms.append("{}{}".format(min_value,max_value))
    return join_pair_of_randoms

def join_pairs_in_string():
    join_random_pair = join_random_pairs()
    pairs_in_string = "{} {} {}".format(join_random_pair[0],join_random_pair[1],join_random_pair[2])
    return pairs_in_string

#if __name__ == "__main__":
#    print(join_pairs_in_string())
#    join_random_pair = join_random_pairs()
#    for e in range(len(join_random_pair)):
#        print(join_random_pair[e],end=' ')