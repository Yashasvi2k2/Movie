import pickle
import requests
import streamlit as st


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7a9169f53e926d9b2b9c9232dfccf2bb&language=en-US'.format(movie_id))
    data=response.json()
    # st.title(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=7a9169f53e926d9b2b9c9232dfccf2bb&language=en-US'.format(movie_id))
    return 'https://image.tmdb.org/t/p/w500/' +data['poster_path']

def recommand(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = simlarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommanded=[]
        recommanded_movies_poster=[]
        for i in movies_list:
            movie_id=movies.iloc[i[0]].movie_id
            #fetch poster
            recommanded.append(movies.iloc[i[0]].title)
            recommanded_movies_poster.append(fetch_poster(movie_id))
        return recommanded,recommanded_movies_poster

movies = pickle.load(open('movies.pkl','rb'))
simlarity = pickle.load(open('simlarity.pkl','rb'))
st.title('Movies Recommender System')

movies_list=pickle.load(open('movies.pkl','rb'))
movies_lists=movies_list['title'].values

option=st.selectbox(
    'Select Your movie',
    movies_lists
)
if st.button('Recommend'):
    names,poster = recommand(option)
    tab1, tab2, tab3,tab4,tab5 = st.columns(5)

    with tab1:
        st.text(names[0])
        st.image(poster[0])

    with tab2:
        st.text(names[1])
        st.image(poster[1])

    with tab3:
        st.text(names[2])
        st.image(poster[2])

    with tab4:
        st.text(names[3])
        st.image(poster[3])

    with tab5:
        st.text(names[4])
        st.image(poster[4])
