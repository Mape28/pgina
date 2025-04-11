@app.route('/canchas', methods=['GET'])
def canchas():
    selected_time = request.args.get('time')
    if selected_time:
        session['time'] = selected_time
    
    reservas = Reserva.query.filter_by(fecha=session.get('date'), hora=selected_time).all()

    canchas_estado = {cancha.nombre: {'imagen': cancha.imagen, 'estado': 'disponible', 'reservado_por': None} for cancha in Cancha.query.all()}

    for reserva in reservas:
        canchas_estado[reserva.cancha]['estado'] = 'reservado'
        canchas_estado[reserva.cancha]['reservado_por'] = reserva.reservado_por

    return render_template('canchass.html', canchas_estado=canchas_estado)
