from flask import Flask, render_template, request
import requests
import pickle
import pandas as pd

app = Flask(__name__)

print("sedang memuat model AI...")
#memuat data film dan matriks kemiripan(model ai)
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
print("Model AI Berhasil dimuat!")

#untuk testing
# #membuat route halaman utama
# @app.route('/')
# def home():
#     return "<h1>Server Sudah Jalan<h1>"

# if __name__ == '__main__':
#     #menjalankan server di port 5000
#     app.run(debug=True)

# fungsi untuk mengambil poster dari TMDB
def fetch_poster(movie_id):
    api_key = "64f89aa9e7f427c5761cee9a97d789b4"
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'

    response = requests.get(url)
    data = response.json()

    #menggabungkan TMBD dengan url dasar gambarnya
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

#fungsi logika rekomendasi untuk web
def recommend(movie) :
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        #simpan judul film
        recommended_movies.append(movies.iloc[i[0]].title)
        #ambil dan simpan poster berdasarkan id
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

#Route Halaman utama
@app.route('/', methods=['GET', 'POST'])
def home():
    #mengambil semua judul film untuk dimasukkan ke dropdown html
    movie_titles = movies['title'].values

    #jika user menekan tombol cari(method POST)
    if request.method == 'POST':
        selected_movie = request.form.get('selected_movie')
        names, posters = recommend(selected_movie)

        # kirim data judul dan poster ke HTML
        return render_template('index.html', movie_titles=movie_titles, names=names, posters=posters, selected_movie=selected_movie)
    
    #jika user baru pertama kali masuk(method GET)
    return render_template('index.html', movie_titles=movie_titles)

if __name__ == '__main__':
    app.run(debug=True)