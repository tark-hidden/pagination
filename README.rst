Pagination
==========
Framework agnostic, very simple and fast URL-generator for pagination.
There will be no python package.

Usage
*****
.. code:: python

    pagination = Pagination(initial_path='/',
                            path='/page-{page}',
                            count=100,
                            per_page=10,
                            page=page,
                            window=10).links()
    return dict(pagination=pagination, ...)

In template you need to write something like

.. code-block:: python

    {% if pagination %}
        <ul class='pagination'>{{ pagination }}</ul>
    {% endif %}



What about AJAX?
****************

Sure enough, you can use it with some tricks.


.. code-block:: javascript

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
***
Pagination(initial_path, path, count, per_page, page, window)

    - initial_path
        The same content with the different URLs is a bad idea.
        / and /?page=1, for example. Initial path is the path without paging.

    - path
        String with {page}, which will be replaced by page number.
        You can define this with url_for function or request.route_path - it is
        your choice. path='/news/2014/01/06/page-{page}' for example.

    - count
        Count of items what you want to show.

    - per_page
        How many items displayed on one page.

    - page
        Current page number (integer)
        Default value: 1

    - window
        How many pages will be shown without '...'
        Default value: 10


Pagination.items()
::
    Returns a list of set with (url, page). With loop you can use it with any
    CSS framework or without it.


Pagination.links()
::
    Returns a string representing pagination list with Bootstrap CSS framework.

    <ul class='pagination'>{{ pagination }}</ul> or
    <div class='pagination'><ul>{{ pagination }}</ul></div> for Bootstrap 2

    where `pagination` is Pagination.links() result.
