list_tohoku=[5349.0,5478.0,5344.0,4644.0,4968.0,6259.0]
list_shikoku=[3148.0,2991.0,2966.0,2457.0]

avg_tohoku=0.0
for yen in list_tohoku:
    avg_tohoku += yen

avg_tohoku /= len(list_tohoku)
print(avg_tohoku)


avg_shikoku=0.0
for yan in list_shikoku:
    avg_shikoku += yan

avg_shikoku /= len(list_shikoku)
print(avg_shikoku)

