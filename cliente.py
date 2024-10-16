import grpc
import factorial_pb2
import factorial_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')  # Conexión local al servidor gRPC
    stub = factorial_pb2_grpc.FactorialServiceStub(channel)

    # Pedir al usuario que ingrese un número
    try:
        user_input = input("Por favor, ingresa un número para calcular su factorial: ").strip()
        number = int(user_input)

        if number < 0:
            print("Por favor, ingresa un número entero no negativo.")
            return

        # Llamar al método CalcularFactorial en el servidor
        response = stub.CalcularFactorial(factorial_pb2.FactorialRequest(number=number))
        print(f'El factorial de {number} es: {response.result}')
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
    except grpc.RpcError as e:
        print(f"Error de RPC: {e.code()} - {e.details()}")  # Manejo de errores de RPC


if __name__ == '__main__':
    run()
