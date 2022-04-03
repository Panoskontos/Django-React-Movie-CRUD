import { useState, useEffect } from "react";
import { ListGroup, Card, Button, Form } from "react-bootstrap";
import api from "./api";

const AddMovie = ({ onAdd }) => {
  const [name, setName] = useState("");
  const [genre, setGenre] = useState("");
  const [starring, setStarring] = useState("");
  const [movieId, setMovieId] = useState(null);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    refreshMovies();
  }, []);

  const refreshMovies = () => {
    api.get("/")
      .then((res) => {
        setMovies(res.data);
        // setName(res[0].name)
        // setGenre(res[0].genre)
        // setStarring(res[0].starring)
        // setMovieId(res[0].id)
      })
      .catch(console.error);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    let item = { name, genre, starring };
    api.post("/", item).then(() => refreshMovies());
  };

  const onUpdate = (id) => {
    let item = { name, genre, starring };
    api.patch(`/${id}/`, item).then((res) => refreshMovies());
  };

  const onDelete = (id) => {
    api.delete(`/${id}/`).then((res) => refreshMovies());
  };

  function selectMovie(id) {
    let item = movies.filter((movie) => movie.id === id)[0];
    setName(item.name);
    setGenre(item.genre);
    setStarring(item.starring);
    setMovieId(item.id);
  }

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-4 myform">
          <h3 className="float-left">Add New Movie</h3>
          <Form onSubmit={onSubmit} className="mt-4">
            <Form.Group className="mb-3" controlId="formBasicName">
              <Form.Label>{movieId}Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicGenre">
              <Form.Label>Genre</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Genre"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicStarring">
              <Form.Label>Starring</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Starring"
                value={starring}
                onChange={(e) => setStarring(e.target.value)}
              />
            </Form.Group>

            <div className="float-right">
              <Button
                variant="primary"
                type="submit"
                onClick={onSubmit}
                className="mx-2"
              >
                Save
              </Button>
              <Button
                variant="primary"
                type="button"
                onClick={() => onUpdate(movieId)}
                className="mx-2"
              >
                Update
              </Button>
            </div>
          </Form>
        </div>
        <div className="col-md-8 m">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Movie Name</th>
                <th scope="col">Genre</th>
                <th scope="col">Starring</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              {movies.map((movie, index) => {
                return (
                  <tr key="">
                    <th scope="row">{movie.id}</th>
                    <td> {movie.name}</td>
                    <td>{movie.genre}</td>
                    <td>{movie.starring}</td>
                    <td className="buttons">
                        <button className="d-inline btn-primary" onClick={() => selectMovie(movie.id)}>
                            Update
                        </button>
                        <button className="d-inline mx-3 btn-danger" onClick={() => onDelete(movie.id)}>
                            Delete
                        </button>
                        
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default AddMovie;