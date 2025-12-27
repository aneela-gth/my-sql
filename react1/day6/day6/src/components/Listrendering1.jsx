
import React from "react";

function Listrendering1() {
    const movies = ["hi nana", "og", "july", "orange"];
    return (
        <>
            <ul>
                {movies.map((name, index) => (
                    <li key={index}>{name}</li>
                ))}
            </ul>
        </>
    );
}

export default Listrendering1;
