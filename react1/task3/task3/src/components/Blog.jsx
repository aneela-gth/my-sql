
function Blog() {
  return (
    <div id="blog">
         <h1 style={{backgroundColor:"greenyellow", textAlign:"center"}}>BLOG</h1>
   
    <div className="blog-page">
       
      {/* LEFT SIDE */}
      <div className="blog-left">
        {/* Blog Item 1 */}
        <div className="blog-card">
          <img
            src="new-chills.png"></img>
          <div className="blog-content">
            <h2>NEW CHILLS FOR SUMMER</h2>
            <p className="date">By Admin on November 28, 2023</p>
            <p>
              You can replace all this text with your own text. You can remove
              any link to our website from this website template.
            </p>
            <button className="read-btn">READ MORE</button>
          </div>
        </div>

        {/* Blog Item 2 */}
        <div className="blog-card">
          <img
            src="berries.png"></img>
          <div className="blog-content">
            <h2>BERRIES ON THE GROVE</h2>
            <p className="date">By Admin on November 28, 2023</p>
            <p>
              You can replace all this text with your own text. You can remove
              any link to our website from this website template.
            </p>
            <button className="read-btn">READ MORE</button>
          </div>
        </div>
      </div>

      {/* RIGHT SIDE */}
      <div className="blog-right">
        <h3>Recent Posts</h3>

        <img
          src="on-diet.png"></img>

        <h4>ON THE DIET</h4>
        <p className="date">By Admin on November 28, 2023</p>
        <p>
          You can replace all this text with your own text. You can remove any
          link to our website.
        </p>
        <button className="read-btn">READ MORE</button>
      </div>
    </div>
     </div>
  );
}

export default Blog;
