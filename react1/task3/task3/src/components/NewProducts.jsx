function NewProduct() {
  return (
    <>
      {/* NEW PRODUCT SECTION */}
      <div className="new-product">
        <div className="text">
          <h5>NEW PRODUCT</h5>
          <h2>The Twist of Healthy Yogurt</h2>
          <p>
            This website template has been designed by
            freewebsitetemplates.com for you, for free.
            You can replace all this text with your own text.
          </p>
        </div>

        <div className="image">
          <img src="yogurt.jpg"></img>
        </div>
      </div>

      {/* ICON BAR */}
      <div className="icon-bar">
        <div>
          <img src="cupcake.png"  width={"80px"}/>
          <p>PRODUCTS</p>
        </div>

        <div className="icon-box">
          <img src="hand.png"  width={"550px"}/>
          <p>OUR STORY</p>
        </div>

        <div className="icon-box">
          <img src="image2.png"  width={"150px"}/>
          <p>FLAVORS</p>
        </div>

        <div className="icon-box">
         <img src="l1.gif"  width={"100px"}/>
          <p>OUR LOCATION</p>
        </div>
      </div>

      {/* FOOTER */}
      <footer className="footer">
        <div className="socials">
          <span><img src="f.png"  width={"30px"}/></span>
          <span><img src="t.png"  width={"30px"}/></span>
          <span><img src="g.png"  width={"30px"}/></span>
          <span><img src="p.png"  width={"30px"}/></span>
        </div>
        <p>© 2023 Freeze. All Rights Reserved.</p>
      </footer>
    </>
  );
}

export default NewProduct;
