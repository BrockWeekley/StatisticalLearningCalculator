import json
import matplotlib.pyplot as plt


class Group:
    def __init__(self, name, probability, categories, posterior_probability, x, y):
        self.name = name
        self.probability = probability,
        self.categories = categories,
        self.posterior_probability = posterior_probability
        self.x = x
        self.y = y


file = open("probabilities2.json")
data = json.load(file)

groups = [Group(**obj) for obj in data["groups"]]
observations = data["observations"]
predictions = data["predictions"]
predictions_x = []
predictions_y = []

count = 0
for count, observation in enumerate(observations):
    predictions_x.append(count)
    prediction_y = 0
    alpha = 0
    for group in groups:
        group.x.append(count)
        group.y.append(group.posterior_probability)
        prediction_y += group.categories[0][predictions[count]] * group.posterior_probability
        group.posterior_probability = group.categories[0][observation] * group.posterior_probability
        alpha += group.posterior_probability
    alpha = 1 / alpha
    predictions_y.append(prediction_y)
    for group in groups:
        group.posterior_probability = group.posterior_probability * alpha

prediction_y = 0
count += 1
for group in groups:
    group.x.append(count)
    group.y.append(group.posterior_probability)
    plt.plot(group.x, group.y, label=group.name)
    prediction_y += group.categories[0][predictions[count]] * group.posterior_probability

predictions_x.append(count)
predictions_y.append(prediction_y)
plt.xticks(groups[0].x)
plt.xlabel("Number of Observations")
plt.ylabel("Posterior Probability of Hypothesis")
plt.legend()
plt.show()

plt.plot(predictions_x, predictions_y)
plt.xlabel("Number of Observations")
plt.ylabel("P(prediction[i] | d)")
plt.show()
file.close()
