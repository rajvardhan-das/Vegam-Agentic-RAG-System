def recursive_chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[str]:
    """
    Recursively split text into overlapping character chunks.
    Preserves paragraphs and sentences where possible.
    """

    separators = ["\n\n", "\n", ". ", " "]

    def split_with_separators(text_block, seps):
        if len(text_block) <= chunk_size:
            return [text_block]

        if not seps:
            return [
                text_block[i:i + chunk_size]
                for i in range(0, len(text_block), chunk_size)
            ]

        sep = seps[0]
        pieces = text_block.split(sep)
        chunks = []
        current = ""

        for piece in pieces:
            if len(current) + len(piece) <= chunk_size:
                current += piece + sep
            else:
                if current:
                    chunks.extend(
                        split_with_separators(current.strip(), seps[1:])
                    )
                current = piece + sep

        if current:
            chunks.extend(
                split_with_separators(current.strip(), seps[1:])
            )

        return chunks

    raw_chunks = split_with_separators(text, separators)

    final_chunks = []
    for i, chunk in enumerate(raw_chunks):
        if i == 0:
            final_chunks.append(chunk)
        else:
            overlap_text = raw_chunks[i-1][-overlap:]
            final_chunks.append(overlap_text + chunk)

    return final_chunks
