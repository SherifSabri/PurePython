from monads import Maybe, Either


def fmap(monadic_value, func):
    """fmap functor for all monadic values"""
    if isinstance(monadic_value, Maybe):
        return Maybe.return_maybe(func(monadic_value.just_value()))

    elif isinstance(monadic_value, Either):
        return Either.return_either(func(monadic_value.right_value()))

    elif isinstance(monadic_value, list):
        for e in monadic_value:
            yield func(e)

