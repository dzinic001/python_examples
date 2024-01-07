#fraktal binär baum

def draw_binary_tree(height):
    if height > 0:
        draw_binary_tree(height - 1)
        print(" " * (height - 1) + "*" + " " * (height - 1))
        draw_binary_tree(height - 1)

# Beispielaufruf
draw_binary_tree(5)
