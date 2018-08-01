from keras.layers.core import Dense


def learning_model(model, input_data, expected_data):
    model.add(Dense(64, input_dim=1, activation='relu'))
    model.add(Dense(16, activation='sigmoid'))
    model.add(Dense(16, activation='sigmoid'))
    model.add(Dense(1, activation='relu'))

    # compile the model
    model.compile(loss='binary_crossentropy', optimizer='SGD', metrics=['accuracy'])

    train_in = input_data
    train_out = expected_data

    print(train_in)
    print(train_out)

    # train the model
    model.fit(train_in, train_out, epochs=100, batch_size=1000)

    # save the model
    model.save("data/model/model.h5")

    # evaluate the model
    loss, accuracy = model.evaluate(train_in, train_out)
    print(loss, accuracy)
