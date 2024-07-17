# Generated from antlr_parser/TinyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TinyCParser import TinyCParser
else:
    from TinyCParser import TinyCParser

# This class defines a complete generic visitor for a parse tree produced by TinyCParser.

class TinyCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TinyCParser#compilationUnit.
    def visitCompilationUnit(self, ctx:TinyCParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#translationUnit.
    def visitTranslationUnit(self, ctx:TinyCParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:TinyCParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:TinyCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declarationList.
    def visitDeclarationList(self, ctx:TinyCParser.DeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:TinyCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#genericSelection.
    def visitGenericSelection(self, ctx:TinyCParser.GenericSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#genericAssocList.
    def visitGenericAssocList(self, ctx:TinyCParser.GenericAssocListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#genericAssociation.
    def visitGenericAssociation(self, ctx:TinyCParser.GenericAssociationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#postfixExpression.
    def visitPostfixExpression(self, ctx:TinyCParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:TinyCParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:TinyCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#unaryOperator.
    def visitUnaryOperator(self, ctx:TinyCParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#castExpression.
    def visitCastExpression(self, ctx:TinyCParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:TinyCParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:TinyCParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#shiftExpression.
    def visitShiftExpression(self, ctx:TinyCParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#relationalExpression.
    def visitRelationalExpression(self, ctx:TinyCParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#equalityExpression.
    def visitEqualityExpression(self, ctx:TinyCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#andExpression.
    def visitAndExpression(self, ctx:TinyCParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:TinyCParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:TinyCParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:TinyCParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:TinyCParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:TinyCParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:TinyCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:TinyCParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#expression.
    def visitExpression(self, ctx:TinyCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#constantExpression.
    def visitConstantExpression(self, ctx:TinyCParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declaration.
    def visitDeclaration(self, ctx:TinyCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:TinyCParser.DeclarationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declarationSpecifiers2.
    def visitDeclarationSpecifiers2(self, ctx:TinyCParser.DeclarationSpecifiers2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:TinyCParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:TinyCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:TinyCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:TinyCParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:TinyCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:TinyCParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structOrUnion.
    def visitStructOrUnion(self, ctx:TinyCParser.StructOrUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:TinyCParser.StructDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structDeclaration.
    def visitStructDeclaration(self, ctx:TinyCParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:TinyCParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:TinyCParser.StructDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#structDeclarator.
    def visitStructDeclarator(self, ctx:TinyCParser.StructDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:TinyCParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#enumeratorList.
    def visitEnumeratorList(self, ctx:TinyCParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#enumerator.
    def visitEnumerator(self, ctx:TinyCParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#enumerationConstant.
    def visitEnumerationConstant(self, ctx:TinyCParser.EnumerationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx:TinyCParser.AtomicTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#typeQualifier.
    def visitTypeQualifier(self, ctx:TinyCParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:TinyCParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx:TinyCParser.AlignmentSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#declarator.
    def visitDeclarator(self, ctx:TinyCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:TinyCParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx:TinyCParser.GccDeclaratorExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx:TinyCParser.GccAttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#gccAttributeList.
    def visitGccAttributeList(self, ctx:TinyCParser.GccAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#gccAttribute.
    def visitGccAttribute(self, ctx:TinyCParser.GccAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx:TinyCParser.NestedParenthesesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#pointer.
    def visitPointer(self, ctx:TinyCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#typeQualifierList.
    def visitTypeQualifierList(self, ctx:TinyCParser.TypeQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:TinyCParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#parameterList.
    def visitParameterList(self, ctx:TinyCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:TinyCParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#identifierList.
    def visitIdentifierList(self, ctx:TinyCParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#typeName.
    def visitTypeName(self, ctx:TinyCParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:TinyCParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:TinyCParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#typedefName.
    def visitTypedefName(self, ctx:TinyCParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#initializer.
    def visitInitializer(self, ctx:TinyCParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#initializerList.
    def visitInitializerList(self, ctx:TinyCParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#designation.
    def visitDesignation(self, ctx:TinyCParser.DesignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#designatorList.
    def visitDesignatorList(self, ctx:TinyCParser.DesignatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#designator.
    def visitDesignator(self, ctx:TinyCParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:TinyCParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#statement.
    def visitStatement(self, ctx:TinyCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#labeledStatement.
    def visitLabeledStatement(self, ctx:TinyCParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#compoundStatement.
    def visitCompoundStatement(self, ctx:TinyCParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#blockItemList.
    def visitBlockItemList(self, ctx:TinyCParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#blockItem.
    def visitBlockItem(self, ctx:TinyCParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:TinyCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#selectionStatement.
    def visitSelectionStatement(self, ctx:TinyCParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#iterationStatement.
    def visitIterationStatement(self, ctx:TinyCParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#forCondition.
    def visitForCondition(self, ctx:TinyCParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#forDeclaration.
    def visitForDeclaration(self, ctx:TinyCParser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#forExpression.
    def visitForExpression(self, ctx:TinyCParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyCParser#jumpStatement.
    def visitJumpStatement(self, ctx:TinyCParser.JumpStatementContext):
        return self.visitChildren(ctx)



del TinyCParser