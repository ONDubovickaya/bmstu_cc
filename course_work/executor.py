import sys
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int


# создание механизма выполнения
# он генерирует JIT код на главном процессоре (host CPU)
# и может быть повторно использован для любого кол-ва модулей
def create_execution_engine():
    # создание целевой машины, представляющей хост
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()

    # механизм выполнения с пустым резервным модулем
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

    return engine


# компилирование LLVM IR строки с помощью созданной машины
# возвращается скомпилированный объект module
def compile_ir(engine, llvm_ir):
    # создание LLVM объекта из IR
    module = llvm.parse_assembly(llvm_ir)
    module.verify()

    # добавление модуля и проверка, что он готов к исполнению
    engine.add_module(module)
    engine.finalize_object()

    return module


def execute(ir_file):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    with open(ir_file) as file:
        llvm_ir = file.read()
        engine = create_execution_engine()

        module = compile_ir(engine, llvm_ir)

        main_type = CFUNCTYPE(c_int)
        main_func = main_type(engine.get_function_address("main"))

        result = main_func()
        return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Wrong command!")
        print("You need to write: ' python executor.py IR_file '")
        print("Example: ' python executor.py example.ll '")
        exit(-1)

    result = execute(sys.argv[1])

    if result is not None:
        print(f"Program exits with code {result}")
