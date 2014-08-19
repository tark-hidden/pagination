Pagination
==========
Framework agnostic, very simple and fast URL-generator for pagination.
There will be no python package.


.. figure:: https://cloud.githubusercontent.com/assets/2255508/3282254/9a63deb6-f4e2-11e3-8c7a-29904a0edf36.png

.. figure:: https://cloud.githubusercontent.com/assets/2255508/3282256/9b0a15b0-f4e2-11e3-80ab-1acea1430d25.png

.. figure:: https://cloud.githubusercontent.com/assets/2255508/3282255/9b086e54-f4e2-11e3-9a4f-56af6e0c9f6d.png


Usage
-----

.. code:: python

    pagination = Pagination(initial_path='/',
                            path='/page-{page}',
                            count=100,
                            per_page=10,
                            page=page,
                            window=10).links()
    return dict(pagination=pagination, ...)

In template you need to write something like

.. code:: python

    {% if pagination %}
        <ul class='pagination'>{{ pagination }}</ul>
    {% endif %}

What about AJAX?
----------------

Sure enough, you can use it with some tricks.

.. code:: javascript

    $(document).on('click', '.pagination a', function(e) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();

        $.get($(this).attr('href'), {}, function(res) {
            ...
        });

        return false;
    });


API
---

.. code:: python

    Pagination(initial_path, path, count, per_page, page, window)

- ``initial_path`` The same content with the different URLs is a bad idea. / and /?page=1, for example. Initial path is the path without paging.

- ``param path`` String with {page}, which will be replaced by page number. You can define this with url_for function or request.route_path - it is your choice. path='/news/2014/01/06/page-{page}' for example.

- ``param count`` Count of items what you want to show.

- ``param per_page`` How many items displayed on one page.

- ``param page`` Current page number (integer). Default value: 1

- ``param window`` How many pages will be shown without '...'. Default value: 10

.. code:: python

    Pagination.items()

- Returns a list of set with (url, page). With loop you can use it with any CSS framework or without it.

.. code:: python

    Pagination.links()
    
- Returns a string representing pagination list with Bootstrap CSS framework.

::

    <ul class='pagination'>{{ pagination }}</ul> or
    <div class='pagination'><ul>{{ pagination }}</ul></div> for Bootstrap 2

    where `pagination` is Pagination.links() result.
