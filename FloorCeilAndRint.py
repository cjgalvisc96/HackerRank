import numpy as np

if __name__ == "__main__":
    _array = np.array(input().split(), float)
    print(
        *[
            str(eval(f"np.{operation}(_array)"))
            for operation in ["floor", "ceil", "rint"]
        ],
        sep="\n",
    )
