from flask import Flask, jsonify, request, Response, render_template
from http import HTTPStatus


app = Flask(__name__)

cards = [
    {
        "id": "0",
        "title": "Default",
        "content": [
            "Some Text1",
            "Some Text2"
        ]
    }
]

# CREATE CARD: PUT
@app.route('/api/cards/<string:requested_card_id>', methods=['PUT'])
def create_card(requested_card_id: str):
    """Handle Create Card endpoint using PUT method.

    If a card with provided ID already exists, it would be updated.
    ID for each card must be unique and provided as a part of URL.
    Card title and content are provided in payload data.
    """
    request_data = request.get_json()
    new_card = next(filter(lambda card: card['id'] == requested_card_id, cards), None)
    if new_card is None:
        new_card = {'id': requested_card_id}
        cards.append(new_card)
    new_card['title'] = request_data.get('title', 'Title not provided')
    new_card['content'] = request_data.get('content', [])
    response = jsonify({'title': new_card['title'], 'content': new_card['content']})
    response.status_code = HTTPStatus.CREATED.value
    return response

# GET CARD: GET
@app.route('/api/cards/<string:requested_card_id>')
def get_card(requested_card_id: str):
    """ Handle Get Card endpoint using GET method. Return title and content of requested card with provided ID. """
    for card in cards:
        if card['id'] == requested_card_id:
            response = jsonify({'title': card['title'], 'content': card['content']})
            response.status_code = HTTPStatus.OK.value
            return response
    # if card ID was not found - return 404 not found error
    response = jsonify({'message': f'Card with id={requested_card_id} was not found!'})
    response.status_code = HTTPStatus.NOT_FOUND.value
    return response

# LIST CARDS: GET
@app.route('/api/pools')
def list_all_cards():
    """ Handle List Cards endpoint using GET method. Return ID and title of all stored cards. """
    # return only ID and Title of each stored card
    response = jsonify({"items": [{'id': card['id'], 'title': card['title']} for card in cards]})
    response.status_code = HTTPStatus.OK.value
    return response

# DELETE CARD: DELETE
@app.route('/api/pools/<string:requested_card_id>', methods=['DELETE'])
def delete_card(requested_card_id: str):
    """ Handle Delete Card endpoint using DELETE method. Rewrite stored cards list excluding card with provided ID. """
    global cards
    # return cards list with all stored cards except the one to remove
    cards = list(filter(lambda card: card['id'] != requested_card_id, cards))
    return Response(status=HTTPStatus.NO_CONTENT.value)

# EDIT CARD: PUT
@app.route('/api/cards/<string:requested_card_id>/edit', methods=['PUT'])
def edit_card(requested_card_id: str):
    """ Handle Edit Card endpoint using PUT method. Update title and content of requested card."""
    request_data = request.get_json()
    for card in cards:
        if card['id'] == requested_card_id:
            card['title'] = request_data.get('title', 'Title not provided')
            card['content'] = request_data.get('content', [])
            response = jsonify({'title': card['title'], 'content': card['content']})
            response.status_code = HTTPStatus.CREATED.value
            return response
    # if card ID was not found - return 404 not found error
    response = jsonify({'message': f'Card with id={requested_card_id} was not found!'})
    response.status_code = HTTPStatus.NOT_FOUND.value
    return response


# WEB UI ALL CARDS VIEW
@app.route('/ui/cards')
def display_cards():
    """Render HTML page with all stored cards listed."""
    # using template from jinja2
    return render_template('webui.html', cards=cards)

# WEB UI SEPARATE CARD VIEW
@app.route('/ui/cards/<string:requested_card_id>')
def display_card_details(requested_card_id: str):
    """Render HTML page with details of card requested by ID."""
    for card in cards:
        if card['id'] == requested_card_id:
            return render_template('webuicard.html', card=card)
    # if card ID was not found - return 404 not found error
    response = jsonify(f'Card with id={requested_card_id} was not found!')
    response.status_code = HTTPStatus.NOT_FOUND.value
    return response


if __name__ == '__main__':
    app.run(port=5000, debug=True)
