import numpy as np
from lightfm import LightFM
from fetch_data import fetch_data


data = fetch_data()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

#model2 = LightFM(loss='logistic')
#model2.fit(data['matrix'], epochs=30, num_threads=2)

#model3 = LightFM(loss='bpr')
#model3.fit(data['matrix'], epochs=30, num_threads=2)

#model4 = LightFM(loss='warp-kos')
#model4.fit(data['matrix'], epochs=30, num_threads=2)


# Get recommendationns function
def get_recommendations(model, coo_mtrx, users_ids):

    n_items = coo_mtrx.shape[1]

    for user in users_ids:

        # Restaurants the model predicts they will like
        scores = model.predict(user, np.arange(n_items))
        top_scores = np.argsort(-scores)[:3]

        print 'Recomendations for user %s:' % user

        for x in top_scores.tolist():
            for restaurant, values in data['restaurants'].iteritems():
                if int(x) == values['id']:
                    print '   - %s' % values['name']
        print '\n' # Get it pretty

        # Restaurants we know they like
        known_positives = data['matrix'].tocsr()[user].indices[:3]
        
        print 'Known positives for user %s:' % user

        for x in known_positives.tolist():
            for artist, values in data['restaurants'].iteritems():
                if int(x) == values['id']:
                    print '   - %s' % values['name']

        print '\n'

user_1 = raw_input('Select user_1 (0 to %s): ' % data['users'])
user_2 = raw_input('Select user_2 (0 to %s): ' % data['users'])
user_3 = raw_input('Select user_3 (0 to %s): ' % data['users'])
print '\n' # Get it pretty

get_recommendations(model, data['matrix'], [user_1, user_2, user_3])


# 2 minutes to run, looks OK
# Now for the ML part: check other models, accuracy
# and visualise

