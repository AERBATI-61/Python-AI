arafat = """\
<div class="page-title-area bg-29">
        <div class="container">
            <div class="page-title-content">
                <h2>Detail Books</h2>
                <ul>
                    <li>
                        <a href="{% url 'index' %}">
                            Home
                        </a>
                    </li>
                    <li class="active">Detail Books</li>
                </ul>
            </div>
        </div>
    </div>

    <section class="product-details-area ptb-100">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 col-md-12">
                    <div class="product-details-image">
                        <img style="max-width: 100%; min-width: 100%; max-height: 650px;min-height: 650px"
                             src="{{ book.image.url }}" alt="Image">
                    </div>
                </div>
                <div class="col-lg-6 col-md-12">
                    <div class="product-details-desc">


                        <ul class="product-summery">
                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Kitabin Adi" disabled="Kitap Adi">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.name }}"
                                                   disabled="{{ book.name }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>



                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Yazar" disabled="Yazar">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.author }}"
                                                   disabled="{{ book.author }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Category" disabled="Category">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.bookcategory }}"
                                                   disabled="{{ book.bookcategory }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>

                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Type" disabled="Type">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.Type }}"
                                                   disabled="{{ book.Type }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Nesir kilgan orun"
                                               disabled="Nesir kilgan orun">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.sender }}"
                                                   disabled="{{ book.sender }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Tarih" disabled="Tarih">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.datetime|date:'Y-m-d H:i' }}"
                                                   disabled="{{ book.datetime|date:'Y-m-d H:i' }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Sayfa" disabled="Sayfa">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.pages }}"
                                                   disabled="{{ book.pages }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <div class="row">
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control" placeholder="Dili" disabled="Dili">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-sm-6">
                                    <div class="form-group">
                                        <div class="form-group">
                                            <input class="form-control" placeholder="{{ book.dill }}"
                                                   disabled="{{ book.dill }}">
                                            <div class="help-block with-errors"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>


                            <h1>


                                <div class="cols-lg-9 col-md-auto">
                                <a href="{{book.file.url}}"><button type="submit" class="default-btn btn-two">
                                            Kitabi indirmek icin
                                        </button></a>


                            </div>
                            </h1>


                        </ul>


                    </div>
                </div>


                <div class="col-lg-12 col-md-12">
                    <div class="tab products-details-tab">
                        <div class="row">


                            <div class="col-lg-12 col-md-12">
                                <div class="tab_content">
                                    <div class="tabs_item">
                                        <div class="products-details-tab-content">
                                            <h3 class="mb-2">{{ book.name }} Hakkinda</h3>
                                            <p>{{ book.subtitle }}</p>
                                            <hr>

                                        </div>
                                    </div>


                                </div>


                            </div>


                        </div>
                    </div>
                </div>


                <h2><ul class="social-wrap ltr">



                    <div class="col-lg-12 col-md-12">
                        <span>Paylas: </span>
                                <a href="https://www.facebook.com/HiraFoundation1/" target="_blank"><button type="submit" class="default-btn btn-two">
                                           <i class="bx bxl-facebook"></i>
                                        </button></a>
                        <a  href="https://www.instagram.com/hirafoundation/"  target="_blank"><button type="submit" class="default-btn btn-two">
                                       <i class="bx bxl-instagram"></i>
                                        </button></a>
                        <a href="https://twitter.com/hira22309952" target="_blank"><button type="submit" class="default-btn btn-two">
                                               <i class="bx bxl-twitter"></i>
                                        </button></a>

                            </div>









                </ul></h2>


            </div>
        </div>
    </section>
"""


ahmet = "mehmet"