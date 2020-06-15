list_tohoku=[5349.0,5478.0,5344.0,4644.0,4968.0,6259.0]
list_shikoku=[3148.0,2991.0,2966.0,2457.0]


avg_shikoku = 0.0
for num in list_shikoku:
    avg_shikoku+=num

avg_shikoku/= len(list_shikoku)
print(avg_shikoku)


