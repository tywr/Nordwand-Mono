def cross_bar_stem(b, rl_ratio, terminal_offset=0, centered_stem=False):
    """(bar left, bar right, stem center, terminal) of a letter with a cross
    bar and a corner ending at a terminal on its right (t, f).

    The bar spans the body, b.x1 to b.x2. The terminal, where the corner
    ends, is terminal_offset * b.width inside the right of the bar. The stem
    splits the bar left to the terminal, rl_ratio of it on its right.
    `centered_stem` moves it all so the stem is on the body's center, as in
    the monospace cell.
    """
    terminal = b.x2 - terminal_offset * b.width
    stem = terminal - rl_ratio * (terminal - b.x1)
    shift = b.xmid - stem if centered_stem else 0
    return b.x1 + shift, b.x2 + shift, stem + shift, terminal + shift
