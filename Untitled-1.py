def main():
    limit = 1
    while limit < 5:
        limit += 1
        if limit == 3:
            continue;
        print(limit, end= ' ')
if __name__ == '__main__':
    main()