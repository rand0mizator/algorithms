def count_sections(sections):
    first_end = sections[0][1]
    solution = [first_end]
    for section in sections[1:]:
        section_start, section_end = section
        if first_end not in range(section_start, section_end + 1):  # if right end for previous section lays not on current section -                                                                     
            solution.append(section_end)                            # so we find all sections covered by this point
            first_end = section_end                                 # taking new right end for search

    return f"{len(solution)}\n{' '.join(map(str,solution))}"


def main():
    sections = []
    quantity = int(input())
    for _ in range(quantity):
        start, end = map(int, input().split())
        sections.append((start, end))
    sections.sort(key=lambda x: x[1])  # sort sections by right end
    print(count_sections(sections))


if __name__ == '__main__':
    main()
