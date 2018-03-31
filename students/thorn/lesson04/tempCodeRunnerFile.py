st put down by advancing
        # the indexes right one spot each.
        first_word = second_word
        second_word = third_word
        trigram_key = (first_word, second_word)
        third_word = trigrams[trigram_key]
        story += f' {third_word}'