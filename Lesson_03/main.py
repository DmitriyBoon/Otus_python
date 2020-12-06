def pow(up_to, e=2):
    results = []
    for i in range(up_to):
        results.append(i ** e)
    return results


print("test", pow(10))
